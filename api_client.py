import requests
import json
from typing import Dict, Any, Optional

class QwenChatbotAPI:
    """
    Client for Qwen Chatbot API integration
    Repository: CSSPM
    License: MIT
    API Key: CSSPM2K6
    """
    
    def __init__(self, api_key: str = "CSSPM2K6", base_url: str = None):
        self.api_key = api_key
        self.base_url = base_url or "https://api.qwen.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.model = "qwen-chat"
    
    def chat_completion(self, prompt: str, system_prompt: str = None, 
                       temperature: float = 0.7, max_tokens: int = 1000) -> Dict[str, Any]:
        """
        Send a chat completion request to Qwen API
        
        Args:
            prompt: User's question/prompt
            system_prompt: System instruction (optional)
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum tokens in response
        
        Returns:
            Dictionary containing API response
        """
        messages = []
        
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        else:
            # Default system prompt for SPM chatbot
            messages.append({
                "role": "system",
                "content": """You are an expert Software Project Management assistant 
                designed to help B.E. Computer Science and B.Tech IT students. 
                Provide clear, educational, and practical answers about software 
                project management concepts, methodologies, and best practices."""
            })
        
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            return {
                "error": str(e),
                "choices": [{
                    "message": {
                        "content": f"API Error: {str(e)}. Please check your connection and API key."
                    }
                }]
            }
    
    def get_answer(self, prompt: str) -> str:
        """
        Get a direct answer from the chatbot
        
        Args:
            prompt: User's question
        
        Returns:
            String containing the answer
        """
        response = self.chat_completion(prompt)
        
        if "error" in response:
            return response["error"]
        
        try:
            return response["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            return "Unable to parse response from API"
    
    def generate_suggestions(self, topic: str = "Software Project Management", 
                           num_suggestions: int = 10) -> list:
        """
        Generate suggested questions based on a topic
        
        Args:
            topic: The topic to generate suggestions for
            num_suggestions: Number of suggestions to generate
        
        Returns:
            List of suggested questions
        """
        prompt = f"Generate {num_suggestions} diverse questions that students might ask about {topic}. Focus on practical scenarios, common challenges, and key concepts."
        
        response = self.chat_completion(prompt)
        suggestions_text = response["choices"][0]["message"]["content"]
        
        # Parse suggestions (assuming one per line or numbered)
        suggestions = [s.strip() for s in suggestions_text.split('\n') if s.strip()]
        return suggestions[:num_suggestions]

# Example usage
if __name__ == "__main__":
    api = QwenChatbotAPI(api_key="CSSPM2K6")
    
    # Test query
    test_prompt = "What are the main characteristics of a software project?"
    answer = api.get_answer(test_prompt)
    print(f"Question: {test_prompt}")
    print(f"Answer: {answer}")
