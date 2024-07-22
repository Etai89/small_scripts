import openai
import time
import settings_file as sf


openai.api_key = sf.API_TOKEN

def get_response(prompt):
  completions = openai.Completion.create(
    engine=sf.ENGINE_TYPE,
    prompt=prompt,
    max_tokens=sf.MAX_TOKENS,
    n=1,
    stop=None,
    temperature=sf.TEMPERATURE_LEVEL,
  )

  message = completions.choices[0].text
  return message.strip()

def main():
    questions = []
    while True:
        subject_question = input("insert the subject of question: ")
        number_questions = input("insert number of questions: ")
        def_questions = input("are we looking for?\nfor 'Questions' choose '1'\nfor 'Problems' choose '2'\nfor 'Quizzes' choose '3'\nto write new one choose '4'\n choose(1/2/3/4):")
        if def_questions == "1":
          def_questions = "questions"
        if def_questions == "2":
          def_questions = "problems"
        if def_questions == "3":
          def_questions = "quizzes"
        if def_questions == "4":
          def_questions = input("write other: ")

        type_question = input(f"choose type of {def_questions}:\nfor 'General' choose '1'\nfor 'Specific' choose '2'\nfor 'Simple' choose '3'\nfor 'Complicated' write '4'\n to Other choose '5'\nchoose (1/2/3/4): ")
        if type_question == "1":
          type_question = "general"
        if type_question == "2":
          type_question = "specific"
        if type_question == "3":
          type_question = "simple"
        if type_question == "4":
          type_question = "complicated"
        if def_questions == "5":
          def_questions = input("write other: ")


        question_start = sf.QUESTIONS_START_WITH
        prompt = f"write a list of {number_questions} different {type_question} {def_questions} about {subject_question} which every question start with {question_start} and end with {sf.QUESTION_END_WITH}"
        print("\nThe Query to Create a Questions list:\n", prompt)
        if prompt == "exit":
            break
        print("\nCreating question list...\n") 
        response = get_response(prompt)
        print("Questions List:\n", response)
        questions.append(response)  # append the response to the questions list

        # ask user if they want to save the questions
        answer = input("\nSave questions? (y/n)")
        if answer.lower() == "y":
            # save questions to file
            with open('chat_info.txt', 'w', encoding='utf-8') as f:
                for q in questions:
                    f.write(q + '\n')
                print("Questions saved to file 'chat_info.txt'!")

            # save questions as list
            questions_list = list(questions)
            print("Questions saved as list: ", questions_list)
            break
        elif answer.lower() == "n":
            print("Questions not saved. Exiting program...")
        else:
            print("Invalid input. Questions not saved. Reload program...")

if __name__ == "__main__":
    main()
