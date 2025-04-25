import allure
import data
import pytest


class TestMainPage:

    @allure.title('Проверка вопросов и ответов')
    @allure.description('Кликаем на вопрос, получаем ответ, сравниваем с ожидаемым ответом')
    @pytest.mark.parametrize( 'question_num' , [ 0, 1, 2, 3, 4, 5, 6, 7 ] )
    def test_answer_for_question(self, main_page, question_num):
        main_page.click_to_question(question_num)
        answer = main_page.get_answer_text(question_num)
        assert answer == data.ANSWERS[question_num]