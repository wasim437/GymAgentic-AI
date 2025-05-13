from crewai import Agent, Task, Crew
from langchain_ollama import OllamaLLM
import os

# 1. Kill any existing Ollama process (Windows)
os.system('taskkill /f /im ollama.exe')

# 2. Configure Ollama connection
os.environ["OLLAMA_HOST"] = "http://localhost:11434"
os.environ["OLLAMA_PROVIDER"] = "ollama"  # Critical for LiteLLM

# 3. Initialize LLM with proper provider format (Using a fitness-related model here)
fitness_llm = OllamaLLM(
    model="ollama/gemma:2b",  # Replace with appropriate fitness model
    base_url="http://localhost:11434",
    temperature=0.7,
    timeout=120
)

# 4. Define multiple agents with different roles
workout_planner = Agent(
    role="Workout Planner",
    goal="Provide personalized workout routines for different fitness levels.",
    backstory="AI trainer with knowledge of various workout types.",
    llm=fitness_llm,
    verbose=True,
    max_iter=3,  # Reduced iterations for simplicity
    max_rpm=2    # Lower rate limit for practical usage
)

diet_advisor = Agent(
    role="Diet Advisor",
    goal="Offer customized diet plans based on fitness goals.",
    backstory="Nutritionist AI who helps plan meals for fitness enthusiasts.",
    llm=fitness_llm,
    verbose=True,
    max_iter=3,
    max_rpm=2
)

motivation_bot = Agent(
    role="Motivation Bot",
    goal="Provide encouragement and motivation for staying fit.",
    backstory="AI assistant that inspires and motivates users on their fitness journey.",
    llm=fitness_llm,
    verbose=True,
    max_iter=3,
    max_rpm=2
)

# 5. Create tasks for each agent
workout_task = Task(
    description="Generate a workout routine for a beginner who wants to lose weight.",
    expected_output="A beginner-friendly workout plan with exercises and durations.",
    agent=workout_planner,
    async_execution=False  # Synchronous execution for local LLM
)

diet_task = Task(
    description="Create a healthy diet plan for someone who wants to build muscle.",
    expected_output="A diet plan with macronutrient breakdown for muscle gain.",
    agent=diet_advisor,
    async_execution=False
)

motivation_task = Task(
    description="Send motivational quotes and affirmations to someone feeling demotivated.",
    expected_output="A set of motivational quotes for someone feeling down.",
    agent=motivation_bot,
    async_execution=False
)

# 6. Configure crew with multiple agents and tasks
crew = Crew(
    agents=[workout_planner, diet_advisor, motivation_bot],
    tasks=[workout_task, diet_task, motivation_task],
    process="sequential",  # Sequential execution for simplicity
    verbose=True
)

# 7. Run with error handling
print("🤖 Starting fitness AI system...")

try:
    # First ensure Ollama is running
    os.system('start /B ollama serve')

    # Run the crew tasks
    result = crew.kickoff()
    print("\n💡 Result:\n", result)

except Exception as e:
    print("\n❌ Error:", e)
   
