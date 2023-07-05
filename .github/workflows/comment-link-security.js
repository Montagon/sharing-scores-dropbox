module.exports = ({github, context}) => {
  manageComments(github, context);
}

function manageComments(github, context) {
    prNumber = context.issue.number
    console.log(prNumber)
    url = github.repositoryUrl +
        "/security/code-scanning?query=pr%3A"+
        prNumber +
        "+tool%3AFormalm+is%3Aopen"
    const body = "FormaLM has performed a code analysis" +
        "and generated a report." +
        "Please check the [Security report]("+url+") "+
        "for more information."
    github.rest.issues.createComment({
      issue_number: prNumber,
      owner: context.repo.owner,
      repo: context.repo.repo,
      body: body
    });
}