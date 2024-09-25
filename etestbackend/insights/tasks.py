from models.drivers import Driver
from models.quizscores import QuizScore

from django_pandas.io import read_frame
import pandas as pd

from celery import shared_task
import json


def get_df_with_column_to_str(df, columns="") -> pd.DataFrame:
    df = df
    df.loc[:columns] = df.loc[:columns].astype(str)
    return df


def get_count_by_date(df, by="", columns_name=["id", "count"]) -> pd.DataFrame:
    groupe_df = (
        df.groupby(pd.to_datetime(df[by]).dt.date)["id"]
        .count()
        .to_frame()
        .rename(columns={"id": "count"})
        .reset_index()
    )

    final_df = get_df_with_column_to_str(groupe_df, columns=by)

    return final_df


@shared_task
def get_results():
    drivers_df = read_frame(Driver.objects.all())
    quizscore_df = read_frame(QuizScore.objects.all())

    test_taken = quizscore_df[quizscore_df["taken"] == True]
    successful_quiz = test_taken[test_taken["score"] >= 50]

    failed_quiz = test_taken[test_taken["score"] < 50]
    pratical_test = quizscore_df[quizscore_df["test_type"] == "Practical"].shape[0]
    theory_test = quizscore_df[quizscore_df["test_type"] == "Theory"].shape[0]

    """return by date"""

    drivers_bydate = get_count_by_date(df=drivers_df, by="created")
    print(drivers_bydate)
    failed_quiz_perdate = get_count_by_date(df=failed_quiz, by="updated")
    successful_quiz_perdate = get_count_by_date(df=successful_quiz, by="updated")

    quiz_scorebyshedule_on = get_count_by_date(df=quizscore_df, by="created")

    quiz_taken_perdate = get_count_by_date(df=test_taken, by="updated")

    results = {
        "number_pratical_test": pratical_test,
        "number_theory_test": theory_test,
        "number_of_candidates": drivers_df.shape[0],
        "scheduled_test": quizscore_df[quizscore_df["schedule_on"].notnull()].shape[0],
        "number_of_test_taken": test_taken.shape[0],
        "number_of_test_failed": failed_quiz.shape[0],
        "number_of_test_passed": successful_quiz.shape[0],
        "registered_driver_perdate": drivers_bydate.to_dict(orient="list"),
        "number_of_scheduled_by_date": quiz_scorebyshedule_on.to_dict(orient="list"),
        "number_of_successful_test_by_date": successful_quiz_perdate.to_dict(
            orient="list"
        ),
        "number_of_failed_test_by_date": failed_quiz_perdate.to_dict(orient="list"),
    }
    return results
