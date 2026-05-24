// =====================================
// FORMAT HOURS
// =====================================

export function formatHours(
  seconds = 0
) {

  const hours =
    seconds / 3600;

  return hours.toFixed(1);
}

// =====================================
// FORMAT PERCENT
// =====================================

export function formatPercent(
  value = 0
) {

  return Math.round(
    value
  );
}

// =====================================
// CALCULATE REMAINING
// =====================================

export function calculateRemainingHours(

  total = 0,
  watched = 0

) {

  return Math.max(
    total - watched,
    0
  );
}

// =====================================
// FILTER PLAYLISTS
// =====================================

export function filterPlaylists(

  playlists = [],
  search = ""

) {

  if (!search.trim()) {

    return playlists;
  }

  return playlists.filter(
    (playlist) =>

      playlist.title
        ?.toLowerCase()
        .includes(
          search.toLowerCase()
        ) ||

      playlist.channel
        ?.toLowerCase()
        .includes(
          search.toLowerCase()
        )
  );
}

// =====================================
// SORT PLAYLISTS
// =====================================

export function sortPlaylists(

  playlists = [],
  mode = "order"

) {

  const cloned =
    [...playlists];

  switch (mode) {

    case "progress":

      return cloned.sort(
        (a, b) =>
          b.yuzde - a.yuzde
      );

    case "hours":

      return cloned.sort(
        (a, b) =>
          b.toplam_saat -
          a.toplam_saat
      );

    case "remaining":

      return cloned.sort(
        (a, b) =>
          b.kalan_gun -
          a.kalan_gun
      );

    case "alphabetical":

      return cloned.sort(
        (a, b) =>
          a.title.localeCompare(
            b.title
          )
      );

    default:

      return cloned;
  }
}

// =====================================
// BUILD PLAYLIST STATS
// =====================================

export function buildPlaylistStats(
  playlists = []
) {

  const totalPlaylists =
    playlists.length;

  const totalHours =
    playlists.reduce(
      (acc, playlist) =>

        acc +
        (playlist.toplam_saat ||
          0),

      0
    );

  const watchedHours =
    playlists.reduce(
      (acc, playlist) =>

        acc +
        (playlist.izlenen_saat ||
          0),

      0
    );

  const averageProgress =
    totalPlaylists > 0
      ? Math.round(

          playlists.reduce(
            (acc, playlist) =>

              acc +
              (playlist.yuzde ||
                0),

            0
          ) / totalPlaylists
        )
      : 0;

  return {

    totalPlaylists,

    totalHours:
      totalHours.toFixed(1),

    watchedHours:
      watchedHours.toFixed(1),

    averageProgress,
  };
}

// =====================================
// VIDEO COUNT
// =====================================

export function countVideos(
  videos = []
) {

  return Array.isArray(
    videos
  )
    ? videos.length
    : 0;
}

// =====================================
// SAFE TEXT
// =====================================

export function safeText(
  value
) {

  if (
    value === null ||
    value === undefined
  ) {

    return "";
  }

  return String(value);
}