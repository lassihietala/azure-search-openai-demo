from typing import IO, AsyncGenerator

from .page import Page
from .parser import Parser


class MarkdownParser(Parser):
    """
    Concrete parser that can parse Markdown files into Page objects. A top-level object becomes a single Page, while a top-level array becomes multiple Page objects.
    """

    async def parse(self, content: IO) -> AsyncGenerator[Page, None]:
        offset = 0
        # Read the Markdown content from the file
        markdown_content = content.read().decode("utf-8")

      # Split the content into sections based on ## level headings
        sections = []
        current_section = ""
        for line in markdown_content.split("\n"):
            if line.startswith("## "):
                # Save the current section and start a new one
                if current_section:
                    sections.append(current_section.strip())
                current_section = line[3:]  # Remove the hash symbols
            else:
                # Append the line to the current section
                current_section += "\n" + line

        # Save the last section
        if current_section:
            sections.append(current_section.strip())

        # Create a Page object for each section
        for i, section in enumerate(sections):

            print("Markdown Section: " + section + "\n\n")

            yield Page(i, offset, section)
            offset += len(section)