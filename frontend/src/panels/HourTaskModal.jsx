import { useState } from "react";

import {
  DndContext,
  closestCenter,
} from "@dnd-kit/core";

import {
  arrayMove,
  SortableContext,
  verticalListSortingStrategy,
  useSortable,
} from "@dnd-kit/sortable";

import { CSS } from "@dnd-kit/utilities";

export default function HourTaskModal({

  block,

  setSelectedBlock,

  calendarDays,

  setCalendarDays,

}) {

  // =====================================
  // SAVE BLOCK
  // =====================================

  function saveBlock(
    updatedBlock
  ) {

    const updated =
      calendarDays.map(
        (day) => ({

          ...day,

          hourBlocks:
            (
              day.hourBlocks ||
              []
            ).map(
              (b) =>

                b.id ===
                updatedBlock.id

                  ? updatedBlock

                  : b
            ),
        })
      );

    setCalendarDays(
      updated
    );

    setLocalBlock(
      updatedBlock
    );

    setSelectedBlock(
      updatedBlock
    );
  }

  // =====================================
  // STATES
  // =====================================

  const [
    localBlock,
    setLocalBlock,
  ] =
    useState({

      ...block,

      tasks:
        block.tasks || [],

      developments:
        block.developments || [],
    });

  const [
    openedDevelopmentId,
    setOpenedDevelopmentId,
  ] =
    useState(null);

  // =====================================
  // ADD ITEM
  // =====================================

  function addItem(
    type
  ) {

    saveBlock({

      ...localBlock,

      [type]: [

        ...(localBlock[type] || []),

        {

          id:
            Date.now(),

          text: "",

          completed:
            false,

          requirements:
            [],
        },
      ],
    });
  }

  // =====================================
  // UPDATE ITEM
  // =====================================

  function updateItem(
    type,
    id,
    field,
    value
  ) {

    saveBlock({

      ...localBlock,

      [type]:
        (
          localBlock[type] ||
          []
        ).map(
          (item) =>

            item.id === id

              ? {

                  ...item,

                  [field]:
                    value,
                }

              : item
        ),
    });
  }

  // =====================================
  // DELETE ITEM
  // =====================================

  function deleteItem(
    type,
    id
  ) {

    saveBlock({

      ...localBlock,

      [type]:
        (
          localBlock[type] ||
          []
        ).filter(
          (item) =>
            item.id !== id
        ),
    });
  }

  // =====================================
  // DRAG END
  // =====================================

  function handleDragEnd(
    event,
    type
  ) {

    const {
      active,
      over,
    } = event;

    if (
      !over ||
      active.id === over.id
    ) {

      return;
    }

    const oldIndex =
      localBlock[
        type
      ].findIndex(
        (i) =>
          i.id === active.id
      );

    const newIndex =
      localBlock[
        type
      ].findIndex(
        (i) =>
          i.id === over.id
      );

    const reordered =
      arrayMove(

        localBlock[type],

        oldIndex,

        newIndex
      );

    saveBlock({

      ...localBlock,

      [type]:
        reordered,
    });
  }

  // =====================================
  // REQUIREMENTS
  // =====================================

  function addRequirement(
    developmentId
  ) {

    saveBlock({

      ...localBlock,

      developments:
        localBlock.developments.map(
          (dev) =>

            dev.id ===
            developmentId

              ? {

                  ...dev,

                  requirements: [

                    ...(dev.requirements || []),

                    {

                      id:
                        Date.now(),

                      text: "",

                      completed:
                        false,
                    },
                  ],
                }

              : dev
        ),
    });
  }

  function updateRequirement(
    developmentId,
    requirementId,
    field,
    value
  ) {

    saveBlock({

      ...localBlock,

      developments:
        localBlock.developments.map(
          (dev) =>

            dev.id ===
            developmentId

              ? {

                  ...dev,

                  requirements:
                    (
                      dev.requirements ||
                      []
                    ).map(
                      (
                        req
                      ) =>

                        req.id ===
                        requirementId

                          ? {

                              ...req,

                              [field]:
                                value,
                            }

                          : req
                    ),
                }

              : dev
        ),
    });
  }

  function deleteRequirement(
    developmentId,
    requirementId
  ) {

    saveBlock({

      ...localBlock,

      developments:
        localBlock.developments.map(
          (dev) =>

            dev.id ===
            developmentId

              ? {

                  ...dev,

                  requirements:
                    (
                      dev.requirements ||
                      []
                    ).filter(
                      (
                        req
                      ) =>

                        req.id !==
                        requirementId
                    ),
                }

              : dev
        ),
    });
  }

  // =====================================
  // TASKS
  // =====================================

  function renderTasks() {

    return (

      <div
        style={{
          marginBottom:
            "30px",
        }}
      >

        <SectionHeader

          title={`Görevler (${
            (
              localBlock.tasks ||
              []
            ).length
          })`}

          onAdd={() =>
            addItem(
              "tasks"
            )
          }

        />

        <DndContext

          collisionDetection={
            closestCenter
          }

          onDragEnd={(event) =>
            handleDragEnd(
              event,
              "tasks"
            )
          }

        >

          <SortableContext

            items={
              (
                localBlock.tasks ||
                []
              ).map(
                (i) => i.id
              )
            }

            strategy={
              verticalListSortingStrategy
            }

          >

            <div>

              {
                (
                  localBlock.tasks ||
                  []
                ).map(
                  (item) => (

                    <SortableTodoItem

                      key={
                        item.id
                      }

                      item={
                        item
                      }

                      type="tasks"

                      updateItem={
                        updateItem
                      }

                      deleteItem={
                        deleteItem
                      }

                    />
                  )
                )
              }

            </div>

          </SortableContext>

        </DndContext>

      </div>
    );
  }

  // =====================================
  // DEVELOPMENTS
  // =====================================

  function renderDevelopments() {

    return (

      <div>

        <SectionHeader

          title={`Geliştirmeler (${
            (
              localBlock.developments ||
              []
            ).length
          })`}

          onAdd={() =>
            addItem(
              "developments"
            )
          }

        />

        <DndContext

          collisionDetection={
            closestCenter
          }

          onDragEnd={(event) =>
            handleDragEnd(
              event,
              "developments"
            )
          }

        >

          <SortableContext

            items={
              (
                localBlock.developments ||
                []
              ).map(
                (i) => i.id
              )
            }

            strategy={
              verticalListSortingStrategy
            }

          >

            <div>

              {
                (
                  localBlock.developments ||
                  []
                ).map(
                  (item) => {

                    const opened =
                      openedDevelopmentId ===
                      item.id;

                    return (

                      <div
                        key={
                          item.id
                        }
                      >

                        <SortableTodoItem

                          item={
                            item
                          }

                          type="developments"

                          updateItem={
                            updateItem
                          }

                          deleteItem={
                            deleteItem
                          }

                          extraButton={

                            <button

                              onClick={() =>

                                setOpenedDevelopmentId(

                                  opened

                                    ? null

                                    : item.id
                                )
                              }

                              style={
                                detailButton
                              }

                            >

                              {
                                opened

                                  ? `Gereksinimleri Kapat (${
                                      (
                                        item.requirements ||
                                        []
                                      ).length
                                    })`

                                  : `Gereksinimler (${
                                      (
                                        item.requirements ||
                                        []
                                      ).length
                                    })`
                              }

                            </button>
                          }

                        />

                        {/* REQUIREMENTS */}

                        {
                          opened && (

                            <div
                              style={{

                                marginLeft:
                                  "50px",

                                marginBottom:
                                  "18px",
                              }}
                            >

                              <div
                                style={{

                                  display:
                                    "flex",

                                  justifyContent:
                                    "space-between",

                                  marginBottom:
                                    "10px",
                                }}
                              >

                                <div
                                  style={{
                                    opacity:
                                      0.7,
                                  }}
                                >

                                  Gereksinimler (
                                  {
                                    (
                                      item.requirements ||
                                      []
                                    ).length
                                  }
                                  )

                                </div>

                                <button

                                  onClick={() =>
                                    addRequirement(
                                      item.id
                                    )
                                  }

                                  style={
                                    addButton
                                  }

                                >

                                  + Gereksinim

                                </button>

                              </div>

                              {
                                (
                                  item.requirements ||
                                  []
                                ).map(
                                  (
                                    req
                                  ) => (

                                    <div
                                      key={
                                        req.id
                                      }

                                      style={{

                                        display:
                                          "flex",

                                        alignItems:
                                          "center",

                                        gap: "12px",

                                        background:
                                          "#151515",

                                        border:
                                          "1px solid #262626",

                                        borderRadius:
                                          "12px",

                                        padding:
                                          "10px",

                                        marginBottom:
                                          "10px",
                                      }}
                                    >

                                      <input

                                        type="checkbox"

                                        checked={
                                          req.completed
                                        }

                                        onChange={(
                                          e
                                        ) =>
                                          updateRequirement(

                                            item.id,

                                            req.id,

                                            "completed",

                                            e
                                              .target
                                              .checked
                                          )
                                        }

                                      />

                                      <input

                                        value={
                                          req.text
                                        }

                                        onChange={(
                                          e
                                        ) =>
                                          updateRequirement(

                                            item.id,

                                            req.id,

                                            "text",

                                            e
                                              .target
                                              .value
                                          )
                                        }

                                        placeholder="
Yeni gereksinim
"

                                        style={
                                          inputStyle
                                        }

                                      />

                                      <button

                                        onClick={() =>
                                          deleteRequirement(

                                            item.id,

                                            req.id
                                          )
                                        }

                                        style={
                                          deleteButton
                                        }

                                      >

                                        Sil

                                      </button>

                                    </div>
                                  )
                                )
                              }

                            </div>
                          )
                        }

                      </div>
                    );
                  }
                )
              }

            </div>

          </SortableContext>

        </DndContext>

      </div>
    );
  }

  // =====================================
  // MAIN
  // =====================================

  return (

    <div
      style={{

        position:
          "fixed",

        inset: 0,

        background:
          "rgba(0,0,0,0.65)",

        display: "flex",

        justifyContent:
          "center",

        alignItems:
          "center",

        zIndex: 9999,
      }}
    >

      <div
        style={{

          width: "900px",

          maxHeight:
            "90vh",

          overflowY:
            "auto",

          background:
            "#111",

          border:
            "1px solid #222",

          borderRadius:
            "22px",

          padding:
            "28px",
        }}
      >

        <div
          style={{

            display: "flex",

            justifyContent:
              "space-between",

            alignItems:
              "center",

            marginBottom:
              "28px",
          }}
        >

          <div>

            <h2
              style={{
                margin: 0,
              }}
            >

              {localBlock.title}

            </h2>

            <div
              style={{

                marginTop:
                  "6px",

                opacity:
                  0.6,
              }}
            >

              {
                localBlock.start
              }

              {" - "}

              {
                localBlock.end
              }

            </div>

          </div>

          <button

            onClick={() =>
              setSelectedBlock(
                null
              )
            }

            style={
              closeButton
            }

          >

            Kapat

          </button>

        </div>

        {renderTasks()}

        {renderDevelopments()}

      </div>

    </div>
  );
}

// =====================================
// SECTION HEADER
// =====================================

function SectionHeader({

  title,
  onAdd,

}) {

  return (

    <div
      style={{

        display: "flex",

        justifyContent:
          "space-between",

        alignItems:
          "center",

        marginBottom:
          "14px",
      }}
    >

      <h3
        style={{
          margin: 0,
        }}
      >

        {title}

      </h3>

      <button

        onClick={onAdd}

        style={addButton}

      >

        + Ekle

      </button>

    </div>
  );
}

// =====================================
// SORTABLE ITEM
// =====================================

function SortableTodoItem({

  item,

  type,

  updateItem,

  deleteItem,

  extraButton,

}) {

  const {

    attributes,

    listeners,

    setNodeRef,

    transform,

    transition,

  } = useSortable({

    id: item.id,
  });

  const style = {

    transform:
      CSS.Transform.toString(
        transform
      ),

    transition,
  };

  return (

    <div

      ref={setNodeRef}

      style={{

        ...style,

        display: "flex",

        alignItems:
          "center",

        gap: "12px",

        background:
          "#181818",

        border:
          "1px solid #262626",

        borderRadius:
          "14px",

        padding:
          "12px",

        marginBottom:
          "10px",
      }}
    >

      <div

        {...attributes}

        {...listeners}

        style={{

          cursor: "grab",

          opacity: 0.5,

          userSelect:
            "none",
        }}
      >

        ☰

      </div>

      <input

        type="checkbox"

        checked={
          item.completed
        }

        onChange={(e) =>
          updateItem(

            type,

            item.id,

            "completed",

            e.target.checked
          )
        }

      />

      <input

        value={item.text}

        onChange={(e) =>
          updateItem(

            type,

            item.id,

            "text",

            e.target.value
          )
        }

        placeholder="Yeni görev..."

        style={inputStyle}

      />

      {extraButton}

      <button

        onClick={() =>
          deleteItem(
            type,
            item.id
          )
        }

        style={
          deleteButton
        }

      >

        Sil

      </button>

    </div>
  );
}

// =====================================
// STYLES
// =====================================

const inputStyle = {

  flex: 1,

  background:
    "#101010",

  color: "white",

  border:
    "1px solid #333",

  borderRadius:
    "10px",

  padding:
    "12px",

  outline:
    "none",
};

const addButton = {

  background:
    "#22c55e",

  color: "black",

  border: "none",

  borderRadius:
    "10px",

  padding:
    "10px 14px",

  fontWeight:
    "bold",

  cursor:
    "pointer",
};

const deleteButton = {

  background:
    "#7f1d1d",

  color: "white",

  border: "none",

  borderRadius:
    "10px",

  padding:
    "10px 12px",

  cursor:
    "pointer",
};

const detailButton = {

  background:
    "#2563eb",

  color: "white",

  border: "none",

  borderRadius:
    "10px",

  padding:
    "10px 12px",

  cursor:
    "pointer",
};

const closeButton = {

  background:
    "#222",

  color: "white",

  border:
    "1px solid #333",

  borderRadius:
    "10px",

  padding:
    "10px 14px",

  cursor:
    "pointer",
};