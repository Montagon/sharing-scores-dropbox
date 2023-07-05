module.exports = ({github, context}) => {
  manageComments(github, context);
}

function manageComments(github, context) {
    url = github.repositoryUrl +
        "/security/code-scanning?query=pr%3A"+
        context.issue.numer +
        "+tool%3AFormalm+is%3Aopen"
    const body = "FormaLM has performed a code analysis" +
        "and generated a report." +
        "Please check the [Security report]("+url+")"+
        "for this."
    github.rest.issues.createComment({
      issue_number: context.issue.number,
      owner: context.repo.owner,
      repo: context.repo.repo,
      body: body
    });
}