module.exports = ({github, context}) => {
  manageComments(github, context);
};

function manageComments(github, context) {
    const modifiedFiles = getModifiedFiles(process.env.DATA);
    addComments(github, context, modifiedFiles);
}

function addComments(github, context, modifiedFiles) {
    const fs = require('fs');
    const execSync = require('child_process').execSync;

    if(fs.existsSync('/home/gradle/reports/')) {
        const files = execSync('find /home/gradle/reports/ -type f').toString().split('\n').filter(Boolean);
//      Create comment pointing to the code analysis report
        commentToCodeAnalysis(github, context);
//      Get the comments pointing to the suggestions and summary
        const comments = reportsToComments(files, modifiedFiles, github, context);
        //  Create the review with the all the comments
        if (comments.length != 0) {
          github.rest.pulls.createReview({
            owner: context.repo.owner,
            repo: context.repo.repo,
            pull_number: context.issue.number,
            commit_id: context.payload.pull_request.head.sha,
            event: 'COMMENT',
            comments: comments
          });
        }
    } else {
//      Create comment explaining that there is no code analysis report
        noReportComment(github, context);
    }
}

function getModifiedFiles(content) {
    const fileLinesMap = new Map();
    jsonContent = JSON.parse(content);
    jsonContent.forEach(diff => {
      const { filename, patch } = diff;

      const patchLines = patch.match(/@@ -\d+,\d+ \+(\d+),(\d+) @@/);
      if (patchLines) {
        const startLine = parseInt(patchLines[1], 10);
        endLine = startLine + parseInt(patchLines[2], 10) - 1;
        if(endLine < 0)
          endLine = 0;
        fileLinesMap.set(filename, { startLine, endLine });
      }
    });
    return fileLinesMap;
}

function check(startLine, endLine, fileLinesMap){
  return startLine >= fileLinesMap.startLine && endLine <= fileLinesMap.endLine;
}

function reportsToComments(files, modifiedFiles, github, context) {
    const fs = require('fs');
    const suggestions = [];
    files.forEach(file => { // report file
      const filename = file.substring(file.lastIndexOf("/") + 1, file.lastIndexOf("."));
      if (filename.startsWith("summary")) {
        const body = fs.readFileSync(file, 'utf8');
        github.rest.issues.createComment({
          issue_number: context.issue.number,
          owner: context.repo.owner,
          repo: context.repo.repo,
          body: body
        });
      } else if (filename.startsWith("suggestion")) {
        const info = filename.split("-");
        const startLine = parseInt(info[info.length - 2]);
        const endLine = parseInt(info[info.length - 1]); // parsing lines from report file's name

        const body = fs.readFileSync(file, 'utf8').split("\n");
        const targetPath = body.shift(); // side-effectful: gets path and removes first line from body
        if(modifiedFiles.has(targetPath) && check(startLine, endLine, modifiedFiles.get(targetPath))){
            if (startLine == endLine) {
                const suggestion = {
                  body: body.join("\n"),
                  path: targetPath,
                  side: "RIGHT",
                  line: startLine
                };
                suggestions.push(suggestion);
            } else {
                const suggestion = {
                  body: body.join("\n"),
                  path: targetPath,
                  side: "RIGHT",
                  start_line: startLine,
                  start_side: "RIGHT",
                  line: endLine
                };
                suggestions.push(suggestion);
            }
        }
      } else {
        console.log(`Unexpected file ${filename}`);
      }
    });
    return suggestions;
}

function noReportComment(github, context) {
    const body = "FormaLM has performed a code analysis " +
            "and it does not have any comments or suggestions for the project.";
    comment = {
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: body
    };
    github.rest.issues.createComment({
      issue_number: context.issue.number,
      owner: context.repo.owner,
      repo: context.repo.repo,
      body: body
    });
}

function commentToCodeAnalysis(github, context) {
    const fs = require('fs');
    const ev = JSON.parse(
      fs.readFileSync(process.env.GITHUB_EVENT_PATH, 'utf8')
    );
    const prNum = ev.pull_request.number;
    url = process.env.URL +
        "/security/code-scanning?query=pr%3A"+
        prNum +
        "+tool%3AFormalm+is%3Aopen";
    const body = "FormaLM has performed a code analysis " +
        "and generated a report. " +
        "Please check the [Security report]("+url+") "+
        "for more information.";
    comment = {
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: body
    };
    github.rest.issues.createComment({
      issue_number: context.issue.number,
      owner: context.repo.owner,
      repo: context.repo.repo,
      body: body
    });
}
