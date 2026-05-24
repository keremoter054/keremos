// =====================================
// API
// =====================================

import api from "./api";

// =====================================
// LOAD HISTORY
// =====================================

export async function loadHistoryService() {

  try {

    const response =
      await api.get(
        "/life/history"
      );

    return response.data;

  } catch (error) {

    console.log(
      "❌ LOAD HISTORY ERROR",
      error
    );

    throw error;
  }
}

// =====================================
// SAVE DAY
// =====================================

export async function saveDayService(
  payload
) {

  try {

    const response =
      await api.post(
        "/life/save-day",
        payload
      );

    return response.data;

  } catch (error) {

    console.log(
      "❌ SAVE DAY ERROR",
      error
    );

    throw error;
  }
}

// =====================================
// LOAD SHIFT CALENDAR
// =====================================

export async function loadShiftCalendarService() {

  try {

    const response =
      await api.get(
        "/shift-calendar"
      );

    return response.data;

  } catch (error) {

    console.log(
      "❌ SHIFT CALENDAR ERROR",
      error
    );

    throw error;
  }
}

// =====================================
// GENERATE SHIFT CALENDAR
// =====================================

export async function generateShiftCalendarService(
  payload
) {

  try {

    const response =
      await api.post(
        "/shift-template/generate",
        payload
      );

    return response.data;

  } catch (error) {

    console.log(
      "❌ GENERATE SHIFT ERROR",
      error
    );

    throw error;
  }
}

// =====================================
// LOAD SHIFT TEMPLATES
// =====================================

export async function loadShiftTemplatesService() {

  try {

    const response =
      await api.get(
        "/shift-template/list"
      );

    return response.data;

  } catch (error) {

    console.log(
      "❌ SHIFT TEMPLATE ERROR",
      error
    );

    throw error;
  }
}

// =====================================
// CREATE SHIFT TEMPLATE
// =====================================

export async function createShiftTemplateService(
  payload
) {

  try {

    const response =
      await api.post(
        "/shift-template/create",
        payload
      );

    return response.data;

  } catch (error) {

    console.log(
      "❌ CREATE SHIFT TEMPLATE ERROR",
      error
    );

    throw error;
  }
}

// =====================================
// ADD SHIFT TEMPLATE DAY
// =====================================

export async function addShiftTemplateDayService(
  payload
) {

  try {

    const response =
      await api.post(
        "/shift-template/day/add",
        payload
      );

    return response.data;

  } catch (error) {

    console.log(
      "❌ ADD SHIFT DAY ERROR",
      error
    );

    throw error;
  }
}