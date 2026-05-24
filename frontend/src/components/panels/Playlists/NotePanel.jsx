import { useEffect, useState } from "react";

import {

  getFullNotes,
  deleteVideoNotes,

} from "../../services/noteService";

export default function NotePanel({

  videoId,
}) {

  // =====================================
  // STATES
  // =====================================

  const [notes, setNotes] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [status, setStatus] =
    useState("");

  // =====================================
  // LOAD
  // =====================================

  useEffect(() => {

    loadNotes();

  }, [videoId]);

  // =====================================
  // LOAD NOTES
  // =====================================

  const loadNotes = async () => {

    try {

      setLoading(true);

      const data =
        await getFullNotes(
          videoId
        );

      setNotes(
        data.notes || ""
      );

    } catch (err) {

      console.error(
        "NOTE LOAD ERROR:",
        err
      );

      setStatus(
        "Note Load Error"
      );

    } finally {

      setLoading(false);
    }
  };

  // =====================================
  // DELETE NOTES
  // =====================================

  const handleDelete =
    async () => {

      try {

        setLoading(true);

        await deleteVideoNotes(
          videoId
        );

        setNotes("");

        setStatus(
          "Notes Deleted"
        );

      } catch (err) {

        console.error(
          "NOTE DELETE ERROR:",
          err
        );

        setStatus(
          "Delete Error"
        );

      } finally {

        setLoading(false);
      }
    };

  // =====================================
  // RENDER
  // =====================================

  return (

    <div
      style={{
        marginTop: "16px",

        background:
          "#111",

        border:
          "1px solid #2a2a2a",

        borderRadius:
          "12px",

        padding: "14px",
      }}
    >

      {/* HEADER */}

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

        <div
          style={{
            fontWeight:
              "bold",

            fontSize:
              "16px",
          }}
        >
          Notes
        </div>

        <button
          onClick={
            handleDelete
          }
          disabled={loading}
          style={{
            background:
              "red",

            color:
              "white",

            border:
              "none",

            borderRadius:
              "8px",

            padding:
              "8px 12px",

            cursor:
              "pointer",
          }}
        >
          Delete
        </button>

      </div>

      {/* STATUS */}

      {status && (

        <div
          style={{
            marginBottom:
              "12px",

            opacity: 0.7,

            fontSize:
              "13px",
          }}
        >
          {status}
        </div>

      )}

      {/* LOADING */}

      {loading && (

        <div
          style={{
            opacity: 0.7,
          }}
        >
          Loading...
        </div>

      )}

      {/* EMPTY */}

      {!loading &&
        !notes && (

        <div
          style={{
            opacity: 0.6,
            fontSize: "13px",
          }}
        >
          Note bulunamadı.
        </div>

      )}

      {/* NOTES */}

      {notes && (

        <div
          style={{
            whiteSpace:
              "pre-wrap",

            lineHeight:
              "1.7",

            fontSize:
              "14px",

            overflowX:
              "auto",
          }}
        >
          {notes}
        </div>

      )}

    </div>
  );
}