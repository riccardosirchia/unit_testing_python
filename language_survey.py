from survey import AnnonymouseSurvey

question = "What programming language do you know?"
my_survey = AnnonymouseSurvey(question)

#show question and store responses
my_survey.show_question()

print("type 'q' to end the program")

while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

print("\n Thank you for your answers")
my_survey.show_results()
