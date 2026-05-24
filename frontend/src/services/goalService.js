// =====================================
// API
// =====================================

import {

  getGoals,

  createGoal as apiCreateGoal,

  addGoalRequirement,

  toggleGoalRequirement,

  predictGoal as apiPredictGoal,

} from "../api/api";

// =====================================
// LOAD GOALS
// =====================================

export async function loadGoalsService({

  setGoals,

  setError,

}) {

  try {

    const data =
      await getGoals();

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
}

// =====================================
// CREATE GOAL
// =====================================

export async function createGoalService({

  goalForm,

  setGoalForm,

  setError,

  loadGoals,

}) {

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

    const data =
      await apiCreateGoal(
        payload
      );

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
}

// =====================================
// ADD REQUIREMENT
// =====================================

export async function addRequirementService({

  goalId,

  textValue,

  goalForm,

  setGoalForm,

  loadGoals,

}) {

  if (
    !textValue.trim()
  )
    return;

  try {

    const data =
      await addGoalRequirement(
        {
          goal_id:
            goalId,

          text:
            textValue,
        }
      );

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
}

// =====================================
// TOGGLE REQUIREMENT
// =====================================

export async function toggleRequirementService({

  todoId,

  loadGoals,

}) {

  try {

    await toggleGoalRequirement(
      todoId
    );

    await loadGoals();

  } catch (err) {

    console.log(
      "❌ TOGGLE REQUIREMENT ERROR",
      err
    );
  }
}

// =====================================
// PREDICT GOAL
// =====================================

export async function predictGoalService({

  goalId,

  setGoalPrediction,

}) {

  try {

    const data =
      await apiPredictGoal(
        goalId
      );

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
}