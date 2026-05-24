import { useState } from "react";

import {

  getFlashcards,
  generateFlashcards,

  deleteFlashcard,
  sendAllFlashcardsToAnki,

} from "../services/flashcardService";

export default function useFlashcards() {

  // =====================================
  // STATES
  // =====================================

  const [flashcards, setFlashcards] =
    useState({});

  const [loadingFlashcards, setLoadingFlashcards] =
    useState(false);

  const [flashcardStatus, setFlashcardStatus] =
    useState("");

  // =====================================
  // LOAD FLASHCARDS
  // =====================================

  const loadFlashcards =
    async (videoId) => {

      try {

        setLoadingFlashcards(true);

        const data =
          await getFlashcards(
            videoId
          );

        setFlashcards((prev) => ({

          ...prev,

          [videoId]:
            data.cards || [],
        }));

      } catch (err) {

        console.error(
          "FLASHCARD LOAD ERROR:",
          err
        );

      } finally {

        setLoadingFlashcards(false);
      }
    };

  // =====================================
  // GENERATE
  // =====================================

  const generateCards =
    async (videoId) => {

      try {

        setFlashcardStatus(
          "Generating..."
        );

        await generateFlashcards(
          videoId
        );

        await loadFlashcards(
          videoId
        );

        setFlashcardStatus(
          "Generated"
        );

      } catch (err) {

        console.error(
          "FLASHCARD GENERATE ERROR:",
          err
        );

        setFlashcardStatus(
          "Generate Error"
        );
      }
    };

  // =====================================
  // DELETE
  // =====================================

  const removeFlashcard =
    async (
      videoId,
      cardId
    ) => {

      try {

        await deleteFlashcard(
          cardId
        );

        await loadFlashcards(
          videoId
        );

      } catch (err) {

        console.error(
          "FLASHCARD DELETE ERROR:",
          err
        );
      }
    };

  // =====================================
  // SEND TO ANKI
  // =====================================

  const sendToAnki =
    async (videoId) => {

      try {

        setFlashcardStatus(
          "Sending To Anki..."
        );

        await sendAllFlashcardsToAnki(
          videoId
        );

        setFlashcardStatus(
          "Sent To Anki"
        );

      } catch (err) {

        console.error(
          "ANKI SEND ERROR:",
          err
        );

        setFlashcardStatus(
          "Anki Error"
        );
      }
    };

  // =====================================
  // CLEAR
  // =====================================

  const clearFlashcards =
    (videoId) => {

      setFlashcards((prev) => ({

        ...prev,

        [videoId]: [],
      }));
    };

  // =====================================
  // RETURN
  // =====================================

  return {

    flashcards,
    setFlashcards,

    loadingFlashcards,

    flashcardStatus,
    setFlashcardStatus,

    loadFlashcards,

    generateCards,

    removeFlashcard,

    sendToAnki,

    clearFlashcards,
  };
}