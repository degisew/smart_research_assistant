from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Parser(BaseModel):
    summary: str = Field(description="summary")
    facts: list[str] = Field(description="facts")

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts
        }


summary_parser = PydanticOutputParser(pydantic_object=Parser)
