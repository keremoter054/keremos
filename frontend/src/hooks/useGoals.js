import {
  useState,
} from "react";

const API =
  "http://127.0.0.1:8000";

export default function useGoals() {

  // =====================================
  // STATES
  // =====================================

  const [goals,
    setGoals] =
    useState([]);

  const [selectedGoalId,
    setSelectedGoalId] =
    useState(null);

  const [goalPrediction,
    setGoalPrediction] =
    useState(null);

  const [error,
    setError] =
    useState("");

  const [goalForm,
    setGoalForm] =
    useState({

      title: "",

      description: "",

      deadline_date: "",

      requirementInput: "",
    });

  // =====================================
  // SELECTED GOAL
  // =====================================

  const selectedGoal =
    goals.find(
      (g) =>
        g.id ===
        selectedGoalId
    ) || null;

  // =====================================
  // HELPERS
  // =====================================

  const calculateGoalProgress =
    (goal) => {

      if (
        !goal?.requirements
      )
        return 0;

      if (
        goal.requirements
          .length === 0
      )
        return 0;

      const completed =
        goal.requirements.filter(
          (r) =>
            r.completed
        ).length;

      return Math.round(
        (
          completed /
          goal.requirements
            .length
        ) * 100
      );
    };

  // =====================================
  // LOAD GOALS
  // =====================================

  const loadGoals =
    async () => {

      try {

        const res =
          await fetch(
            `${API}/goals`
          );

        const data =
          await res.json();

        if (
          !Array.isArray(
            data
          )
        ) {

          throw new Error(
            "Goals response array değil"
          );
        }

        setGoals(data);

      } catch (err) {

        console.log(
          "❌ GOALS ERROR",
          err
        );

        setError(
          "Goals yüklenemedi"
        );
      }
    };

  // =====================================
  // CREATE GOAL
  // =====================================

  const createGoal =
    async () => {

      if (
        !goalForm.title.trim()
      ) {

        setError(
          "Goal başlığı boş olamaz"
        );

        return;
      }

      try {

        setError("");

        const payload = {

          title:
            goalForm.title,

          description:
            goalForm.description,

          deadline_date:
            goalForm.deadline_date,
        };

        const res =
          await fetch(
            `${API}/goals/create`,
            {
              method: "POST",

              headers: {
                "Content-Type":
                  "application/json",
              },

              body:
                JSON.stringify(
                  payload
                ),
            }
          );

        const data =
          await res.json();

        if (
          data.status !==
          "ok"
        ) {

          throw new Error(
            data.error ||
              "Goal oluşturulamadı"
          );
        }

        await loadGoals();

        setGoalForm({

          title: "",

          description: "",

          deadline_date: "",

          requirementInput:
            "",
        });

      } catch (err) {

        console.log(
          "❌ CREATE GOAL ERROR",
          err
        );

        setError(
          err.message
        );
      }
    };

  // =====================================
  // ADD REQUIREMENT
  // =====================================

  const addRequirement =
    async (
      goalId,
      textValue
    ) => {

      if (
        !textValue.trim()
      )
        return;

      try {

        const res =
          await fetch(
            `${API}/goal-todos/add`,
            {
              method:
                "POST",

              headers: {
                "Content-Type":
                  "application/json",
              },

              body:
                JSON.stringify({
                  goal_id:
                    goalId,

                  text:
                    textValue,
                }),
            }
          );

        const data =
          await res.json();

        if (
          data.status !==
          "ok"
        ) {

          throw new Error(
            data.error ||
              "Requirement eklenemedi"
          );
        }

        await loadGoals();

        setGoalForm({

          ...goalForm,

          requirementInput:
            "",
        });

      } catch (err) {

        console.log(
          "❌ REQUIREMENT ERROR",
          err
        );
      }
    };

  // =====================================
  // TOGGLE REQUIREMENT
  // =====================================

  const toggleRequirement =
    async (
      todoId
    ) => {

      try {

        await fetch(
          `${API}/goal-todos/toggle/${todoId}`,
          {
            method: "PUT",
          }
        );

        await loadGoals();

      } catch (err) {

        console.log(
          "❌ TOGGLE REQUIREMENT ERROR",
          err
        );
      }
    };

  // =====================================
  // PREDICT GOAL
  // =====================================

  const predictGoal =
    async (
      goalId
    ) => {

      try {

        const res =
          await fetch(
            `${API}/goals/predict/${goalId}`
          );

        const data =
          await res.json();

        setGoalPrediction(
          data
        );

      } catch (err) {

        console.log(
          "❌ PREDICTION ERROR",
          err
        );

        setGoalPrediction({
          status: "error",
        });
      }
    };

  // =====================================
  // RETURN
  // =====================================

  return {

    goals,
    setGoals,

    selectedGoalId,
    setSelectedGoalId,

    selectedGoal,

    goalPrediction,
    setGoalPrediction,

    goalForm,
    setGoalForm,

    calculateGoalProgress,

    loadGoals,

    createGoal,

    addRequirement,

    toggleRequirement,

    predictGoal,

    error,
  };
}