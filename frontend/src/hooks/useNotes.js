import { useState } from "react";

import {

  getFullNotes,

  deleteVideoNotes,

  generateVideoNotes,

} from "../services/noteService";

export default function useNotes() {

  // =====================================
  // STATES
  // =====================================

  const [notesMap, setNotesMap] =
    useState({});

  const [loadingNotes, setLoadingNotes] =
    useState(false);

  const [noteStatus, setNoteStatus] =
    useState("");

  // =====================================
  // LOAD NOTES
  // =====================================

  const loadNotes =
    async (videoId) => {

      try {

        setLoadingNotes(true);

        const data =
          await getFullNotes(
            videoId
          );

        setNotesMap((prev) => ({

          ...prev,

          [videoId]:
            data.notes || "",
        }));

      } catch (err) {

        console.error(
          "NOTE LOAD ERROR:",
          err
        );

      } finally {

        setLoadingNotes(false);
      }
    };

  // =====================================
  // GENERATE NOTES
  // =====================================

  const generateNotes =
    async (videoId) => {

      try {

        setNoteStatus(
          "Generating..."
        );

        await generateVideoNotes(
          videoId
        );

        setNoteStatus(
          "Generation Started"
        );

      } catch (err) {

        console.error(
          "NOTE GENERATE ERROR:",
          err
        );

        setNoteStatus(
          "Generate Error"
        );
      }
    };

  // =====================================
  // DELETE NOTES
  // =====================================

  const removeNotes =
    async (videoId) => {

      try {

        await deleteVideoNotes(
          videoId
        );

        setNotesMap((prev) => ({

          ...prev,

          [videoId]: "",
        }));

        setNoteStatus(
          "Deleted"
        );

      } catch (err) {

        console.error(
          "NOTE DELETE ERROR:",
          err
        );

        setNoteStatus(
          "Delete Error"
        );
      }
    };

  // =====================================
  // CLEAR NOTES
  // =====================================

  const clearNotes =
    (videoId) => {

      setNotesMap((prev) => ({

        ...prev,

        [videoId]: "",
      }));
    };

  // =====================================
  // RETURN
  // =====================================

  return {

    notesMap,
    setNotesMap,

    loadingNotes,

    noteStatus,
    setNoteStatus,

    loadNotes,

    generateNotes,

    removeNotes,

    clearNotes,
  };
}