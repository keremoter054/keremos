// =====================================
// ARRAY MOVE
// =====================================

export function arrayMoveCustom(

  array,
  fromIndex,
  toIndex

) {

  const newArray =
    [...array];

  const [movedItem] =
    newArray.splice(
      fromIndex,
      1
    );

  newArray.splice(
    toIndex,
    0,
    movedItem
  );

  return newArray;
}

// =====================================
// FIND INDEX BY ID
// =====================================

export function findIndexById(
  array,
  id
) {

  return array.findIndex(
    (item) =>
      item.id === id
  );
}

// =====================================
// REORDER PLAYLISTS
// =====================================

export function reorderPlaylistsLocal(

  items,
  activeId,
  overId

) {

  if (
    activeId === overId
  ) {

    return items;
  }

  const oldIndex =
    findIndexById(
      items,
      activeId
    );

  const newIndex =
    findIndexById(
      items,
      overId
    );

  if (
    oldIndex === -1 ||
    newIndex === -1
  ) {

    return items;
  }

  return arrayMoveCustom(

    items,

    oldIndex,
    newIndex
  );
}

// =====================================
// BUILD ORDER PAYLOAD
// =====================================

export function buildOrderPayload(
  items
) {

  return items.map(
    (item) => item.id
  );
}