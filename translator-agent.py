from agents import Agent, Runner
from connection import config

# Create an agent named "Translator" with specific instructions.
translator_agent: Agent = Agent(
    name="Translator",
    instructions="You are a professional translator. Your task is to translate any text provided from English to Hindi. Only provide the translated text without any additional conversational text or explanations."
)

# The text you want to translate.
text_to_translate = "Hello, how are you today? I hope you are having a great day!"

# Run the agent with the text to be translated.
result = Runner.run_sync(translator_agent, text_to_translate, run_config=config)

# Print the final translated output.
print(result.final_output)