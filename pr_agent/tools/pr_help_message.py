from pr_agent.config_loader import get_settings
from pr_agent.git_providers import get_git_provider
from pr_agent.log import get_logger


class PRHelpMessage:
    def __init__(self, pr_url: str, args=None, ai_handler=None):
        self.git_provider = get_git_provider()(pr_url)

    async def run(self):
        try:
            get_logger().info('Getting PR Help Message...')
            pr_comment="## PR Agent Intro\n\n"
            pr_comment +="🤖 Welcome to the PR Agent, an AI-powered tool for automated pull request analysis, feedback, suggestions and more."""
            pr_comment +="\n\nHere are the tools you can use to interact with the PR Agent:\n"
            base_path ="https://github.com/Codium-ai/pr-agent/tree/main/docs"
            pr_comment +=f"""\
\n\n
- [DESCRIBE]({base_path}/DESCRIBE.md)
- [REVIEW]({base_path}/REVIEW.md)
- [IMPROVE]({base_path}/IMPROVE.md)
- [ASK]({base_path}/ASK.md)
- [SIMILAR_ISSUE]({base_path}/SIMILAR_ISSUE.md)
- [UPDATE CHANGELOG]({base_path}/UPDATE_CHANGELOG.md)
- [ADD DOCUMENTATION]({base_path}/ADD_DOCUMENTATION.md)
- [GENERATE CUSTOM LABELS]({base_path}/GENERATE_CUSTOM_LABELS.md)
- [Analyze]({base_path}/Analyze.md)
- [Test]({base_path}/TEST.md)
- [CI Feedback]({base_path}/CI_FEEDBACK.md)
"""
            pr_comment +=f"""\n\nNote that each command be [applied automatically](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#github-app-automatic-tools-for-pr-actions) when a new PR is opened, or invoked manually by [commenting on a PR](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#online-usage)."""
            if get_settings().config.publish_output:
                self.git_provider.publish_comment(pr_comment)
        except Exception as e:
            get_logger().error(f"Error while running PRHelpMessage: {e}")
        return ""