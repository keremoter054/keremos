// =====================================
// CLONE TODO
// =====================================

export function cloneTodo(
  todo
) {

  return {

    ...todo,

    id:
      Date.now() +
      Math.random(),
  };
}

// =====================================
// CLONE TASK
// =====================================

export function cloneTask(
  task
) {

  return {

    ...task,

    id:
      Date.now() +
      Math.random(),

    todos:
      (task.todos || []).map(
        cloneTodo
      ),
  };
}

// =====================================
// CLONE DAY
// =====================================

export function cloneDay(
  day
) {

  return {

    ...day,

    tasks:
      (day.tasks || []).map(
        cloneTask
      ),
  };
}