import subprocess
import time

def call_ai(cli_command, prompt):
    """Executes the specific CLI command with the given prompt."""
    try:
        # result = subprocess.run([cli_command, "-p", prompt], capture_output=True, text=True, check=True)
        # Note: Adjust the flag (-p, --prompt, etc.) based on your specific CLI version
        result = subprocess.run(
            [cli_command, prompt], 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error calling {cli_command}: {str(e)}"

def start_dialogue(initial_prompt, rounds=3):
    current_prompt = initial_prompt
    
    print(f"\n🚀 Starting Dialogue with: {initial_prompt}\n")
    
    for i in range(1, rounds + 1):
        print(f"--- ROUND {i} ---")
        
        # Phase 1: Claude responds to the current prompt
        print("\n[CLAUDE IS THINKING...]")
        claude_response = call_ai("claude", current_prompt)
        print(f"CLAUDE: {claude_response}\n")
        
        # Phase 2: Gemini reviews or responds to Claude
        # We wrap Claude's response in a directive for Gemini
        gemini_instruction = f"Review and critique the following response from Claude. If there are errors, point them out. If it is good, expand on it: {claude_response}"
        
        print("[GEMINI IS THINKING...]")
        gemini_response = call_ai("gemini", gemini_instruction)
        print(f"GEMINI: {gemini_response}\n")
        
        # Prepare the next round's prompt based on Gemini's feedback
        current_prompt = f"Gemini said your previous answer had these points: {gemini_response}. Please provide an updated response."
        
        time.sleep(1) # Small delay to prevent API rate limiting

if __name__ == "__main__":
    topic = input("Enter a topic or problem for the AIs to solve: ")
    rounds_count = int(input("How many rounds of interaction? (e.g., 2 or 3): "))
    start_dialogue(topic, rounds=rounds_count)
