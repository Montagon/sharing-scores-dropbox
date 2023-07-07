module.exports = ({github, context}) => {
  manageComments(github, context);
}

function manageComments(github, context) {
    const modifiedFiles = getModifiedFiles(process.env.DATA);
    addComments(github, context, modifiedFiles);
}

function addComments(github, context, modifiedFiles) {
    const fs = require('fs');
    const execSync = require('child_process').execSync;
    files = []
    if(fs.existsSync('/home/gradle/reports/')) {
        files = execSync('find /home/gradle/reports/ -type f').toString().split('\n').filter(Boolean);
    }

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
            if (startLine >= endLine) {
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

    if (suggestions.length != 0) {
      github.rest.pulls.createReview({
        owner: context.repo.owner,
        repo: context.repo.repo,
        pull_number: context.issue.number,
        commit_id: context.payload.pull_request.head.sha,
        event: 'COMMENT',
        comments: suggestions
      });
    }
}

function getModifiedFiles(content) {
    const fileLinesMap = new Map();
    jsonContent = JSON.parse(content)
    jsonContent.forEach(diff => {
      const { filename, patch } = diff;

      const patchLines = patch.match(/@@ -\d+,\d+ \+(\d+),(\d+) @@/);
      if (patchLines) {
        const startLine = parseInt(patchLines[1], 10);
        endLine = startLine + parseInt(patchLines[2], 10) - 1;
        if(endLine < 0)
          endLine = 0
        fileLinesMap.set(filename, { startLine, endLine });
      }
    });
    return fileLinesMap;
}

function check(startLine, endLine, fileLinesMap){
  return startLine >= fileLinesMap.startLine && endLine <= fileLinesMap.endLine;
}
