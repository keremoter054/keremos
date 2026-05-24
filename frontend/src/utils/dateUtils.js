// =====================================
// START DATE
// =====================================

export function getStartDate() {

  const d = new Date();

  d.setHours(
    0,
    0,
    0,
    0
  );

  return d;
}

// =====================================
// GET DATE FOR DAY
// =====================================

export function getDateForDay(
  dayNumber,
  startDate = getStartDate()
) {

  return new Date(

    startDate.getTime() +

    (dayNumber - 1) *

    86400000
  );
}

// =====================================
// FORMAT DATE TR
// =====================================

export function formatDateTR(
  date
) {

  return date.toLocaleDateString(
    "tr-TR"
  );
}

// =====================================
// FORMAT DATE SQL
// =====================================

export function formatDateSQL(
  date
) {

  return date.toLocaleDateString(
    "sv-SE"
  );
}

// =====================================
// GET TODAY STRING
// =====================================

export function getTodayString() {

  return formatDateSQL(
    new Date()
  );
}

// =====================================
// ADD DAYS
// =====================================

export function addDays(
  date,
  days
) {

  const d =
    new Date(date);

  d.setDate(
    d.getDate() + days
  );

  return d;
}

// =====================================
// DAY DIFFERENCE
// =====================================

export function diffDays(
  date1,
  date2
) {

  const ms =
    Math.abs(
      date2 - date1
    );

  return Math.floor(
    ms / 86400000
  );
}