import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

import probability_simulator.logic as probability_logic
import visual_simulator.logic as visual_logic


def day_to_date(day_number):
    """
    Converts a day number from 1 to 365
    into e month and day.
    """

    start_date = datetime(2023, 1, 1)

    birthday_date = start_date + timedelta(
        days=day_number - 1
    )

    return birthday_date.strftime("%B %d")



st.set_page_config(
    page_title="Birthday Paradox",
    page_icon="🎂",
    layout="wide"
)



st.sidebar.title("🎂 Birthday Paradox")

st.sidebar.write(
    "Choose a simulator:"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Probability Simulator",
        "👥 Visual Simulator"
    ]
)



if page == "📊 Probability Simulator":

    st.title("📊 Birthday Paradox Probability Simulator")

    st.write(
        "This simulator runs the birthday paradox experiment "
        "multiple times and estimates the probability of "
        "at least two people sharing the same birthday."
    )

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/d/dd/Birthday_candles.jpg",
        use_container_width=True
    )




    people = st.number_input(
        "Enter number of people:",
        min_value=2,
        max_value=1000,
        value=23
    )

    trials = st.number_input(
        "Enter number of trials:",
        min_value=1,
        max_value=10000000,
        value=1000
    )




    if st.button("Calculate Probability"):

        result = probability_logic.examination(
            people,
            trials
        )

        st.success(
            f"The probability of shared birthdays is: "
            f"{result:.4f}%"
        )



        fig, ax = plt.subplots()

        ax.bar(
            [
                "Shared Birthday",
                "No Shared Birthday"
            ],
            [
                result,
                100 - result
            ],
            color=[
                "tomato",
                "skyblue"
            ]
        )

        ax.set_ylabel(
            "Probability (%)"
        )

        ax.set_title(
            "Birthday Paradox Probability"
        )

        st.pyplot(fig)

        st.balloons()




    st.subheader(
        "Probability by Number of People"
    )

    data = []

    for num_people in range(0, 101):

        if num_people < 2:

            data.append(0)

        else:

            result = probability_logic.examination(
                num_people,
                100
            )

            data.append(result)


    df = pd.DataFrame(
        {
            "Number of People": range(0, 101),
            "Probability (%)": data
        }
    )


    st.line_chart(
        df.rename(
            columns={
                "Number of People": "index"
            }
        ).set_index("index")
    )



elif page == "👥 Visual Simulator":

    st.title("👥 Visual Birthday Simulator")

    st.write(
        "Generate birthdays for a group of people "
        "and see if any of them share the same birthday."
    )

    people = st.number_input(
        "Enter number of people:",
        min_value=1,
        max_value=100,
        value=23,
        key="visual_people"
    )


    if st.button(
        "🎲 Generate Birthdays",
        key="generate_birthdays"
    ):

        birthdays = visual_logic.generate_birthdays(
            people
        )

        matches = visual_logic.find_matches(
            birthdays
        )

        st.session_state.birthdays = birthdays

        st.session_state.matches = matches



    if "birthdays" in st.session_state:

        birthdays = st.session_state.birthdays

        matches = st.session_state.matches




        if matches:

            st.success(
                "🎉 Shared birthday found!"
            )

        else:

            st.info(
                "❌ No shared birthdays "
            )



        matched_people = set()

        for birthday, people_indices in matches.items():

            for person_index in people_indices:

                matched_people.add(
                    person_index
                )




        st.subheader(
            "👥 People and Their Birthdays"
        )



        row_count = (
            len(birthdays) + 4
        ) // 5


        for row in range(row_count):

            columns = st.columns(5)


            for column_index in range(5):

                person_index = (
                    row * 5
                    + column_index
                )



                if person_index >= len(
                    birthdays
                ):

                    break


                birthday = birthdays[
                    person_index
                ]


                birthday_date = day_to_date(
                    birthday
                )


                with columns[column_index]:

                    with st.container(
                        border=True
                    ):

                        st.write("🧑")

                        st.write(
                            f"**Person "
                            f"{person_index + 1}**"
                        )

                        st.write(
                            f"🎂 "
                            f"{birthday_date}"
                        )


                        if person_index in matched_people:

                            st.success(
                                "🎉 MATCH"
                            )



        if matches:

            st.subheader(
                "🎉 Matching Birthdays"
            )


            for (
                birthday,
                people_indices
            ) in matches.items():

                birthday_date = day_to_date(
                    birthday
                )


                with st.container(
                    border=True
                ):

                    st.write(
                        f"🎂 **{birthday_date}**"
                    )


                    for person_index in (
                        people_indices
                    ):

                        st.write(
                            f"🧑 Person "
                            f"{person_index + 1}"
                        )