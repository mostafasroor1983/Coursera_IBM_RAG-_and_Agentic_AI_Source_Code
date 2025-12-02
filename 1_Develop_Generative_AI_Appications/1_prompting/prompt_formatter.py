class PromptFormatter:
    """Utility class for formatting prompts with variables."""

    def __init__(self, prompt_template):
        """
        Initialize with a ChatPromptTemplate.

        Args:
            prompt_template: A ChatPromptTemplate instance
        """
        self.prompt = prompt_template

    def format(self, variables):
        """
        Format the prompt with given variables.

        Args:
            variables: Dictionary of variables to fill in the template

        Returns:
            Formatted prompt string
        """
        return self.prompt.format(**variables)

    def format_and_print(self, variables):
        """
        Format the prompt and print it for debugging.

        Args:
            variables: Dictionary of variables to fill in the template

        Returns:
            Formatted prompt string
        """
        formatted = self.format(variables)
        print(formatted)
        return formatted
