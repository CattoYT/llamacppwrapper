from llama_cpp import Llama
class llamaLLM:
    def __init__(self, systemprompt, model="bartowski/Meta-Llama-3-8B-Instruct-GGUF", filename="Meta-Llama-3-8B-Instruct-Q4_K_M.gguf"):
        

        self.messages = [
          {"role": "system", "content": systemprompt},
        ]

        self.llm = Llama.from_pretrained(
          repo_id=model,
          filename=filename,
          verbose=False,
          n_gpu_layers=-1, 
          n_ctx=4096
        )
    def addToConversation(self, content, role):
        self.messages.append(
              {
                  "role": role,
                  "content": content
              }
          )
