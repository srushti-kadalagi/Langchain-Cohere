from langchain_community.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from load_drive_doc import text_content  # Import the text from Google Drive

# Set up Cohere API
cohere_api_key = "t3h2NuHyMNLBBEtjKzsMQDPA5JEokWoMTwKGAvPP"
llm = Cohere(cohere_api_key=cohere_api_key, model="command")

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["document"],
    template="Summarize the following text:\n\n{document}\n\nSummary:"
)

# Create a chain to process text
chain = LLMChain(llm=llm, prompt=prompt_template)

# Run the model
output = chain.run(document=text_content)
print("\nGenerated Summary:\n", output)
