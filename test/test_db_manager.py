from src.db_manager import DBManager


def test_get_companies_and_vacancies_count(mocker):
    db_manager = DBManager()
    mocker.patch.object(db_manager.cur, 'fetchall', return_value=[("Company1", 10), ("Company2", 15)])
    result = db_manager.get_companies_and_vacancies_count()
    assert result == [("Company1", 10), ("Company2", 15)]


def test_get_all_vacancies(mocker):
    db_manager = DBManager()
    mocker.patch.object(db_manager.cur, 'fetchall', return_value=[("Company1", "Job1", 50000, "job1_url"), ("Company2", "Job2", 60000, "job2_url")])
    result = db_manager.get_all_vacancies()
    assert result == [("Company1", "Job1", 50000, "job1_url"), ("Company2", "Job2", 60000, "job2_url")]


def test_get_avg_salary(mocker):
    db_manager = DBManager()
    mocker.patch.object(db_manager.cur, 'fetchall', return_value=[(55000,)])
    result = db_manager.get_avg_salary()
    assert result == [(55000,)]


def test_get_vacancies_with_higher_salary(mocker):
    db_manager = DBManager()
    mocker.patch.object(db_manager.cur, 'fetchall', return_value=[("Job1", 60000), ("Job2", 70000)])
    result = db_manager.get_vacancies_with_higher_salary()
    assert result == [("Job1", 60000), ("Job2", 70000)]


def test_get_vacancies_with_keyword(mocker):
    db_manager = DBManager()
    keyword = "Python"
    mocker.patch.object(db_manager.cur, 'fetchall', return_value=[("Python Developer", 60000, "python_dev_url")])
    result = db_manager.get_vacancies_with_keyword(keyword)
    assert result == [("Python Developer", 60000, "python_dev_url")]
