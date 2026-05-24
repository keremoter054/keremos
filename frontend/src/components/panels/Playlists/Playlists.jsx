import { useEffect, useState } from "react";

import {
  DndContext,
  closestCenter,
} from "@dnd-kit/core";

import {
  SortableContext,
  verticalListSortingStrategy,
} from "@dnd-kit/sortable";

import PlaylistCard from "./PlaylistCard";

import VideoItem from "./VideoItem";

import PlaylistHeader from "./PlaylistHeader";

import {
  fetchPlaylists,
  fetchPlaylistVideos,
} from "../../services/playlistService";

export default function Playlists({

  setPlanBitis,
  setGlobalPercent,

  selectedVideo,
  setSelectedVideo,
}) {

  // =====================================
  // STATES
  // =====================================

  const [items, setItems] =
    useState([]);

  const [dailyTarget, setDailyTarget] =
    useState(0);

  const [openPlaylistId, setOpenPlaylistId] =
    useState(null);

  const [videosMap, setVideosMap] =
    useState({});

  // =====================================
  // LOAD PLAYLISTS
  // =====================================

  useEffect(() => {

    loadPlaylists();

  }, []);

  // =====================================
  // LOAD PLAYLISTS FUNCTION
  // =====================================

  const loadPlaylists = async () => {

    try {

      const data =
        await fetchPlaylists();

      const playlistList =
        Array.isArray(data)
          ? data
          : data.playlists || [];

      setItems(playlistList);

      setDailyTarget(
        data.daily_target ||
        data.gunluk_hedef_saat ||
        0
      );

      setPlanBitis?.(
        data.plan_bitis
      );

      setGlobalPercent?.(
        data.global_percent
      );

    } catch (err) {

      console.error(
        "PLAYLIST LOAD ERROR:",
        err
      );
    }
  };

  // =====================================
  // LOAD VIDEOS
  // =====================================

  const loadVideos = async (
    playlistId
  ) => {

    try {

      const data =
        await fetchPlaylistVideos(
          playlistId
        );

      setVideosMap((prev) => ({

        ...prev,

        [playlistId]: data,
      }));

    } catch (err) {

      console.error(
        "VIDEO LOAD ERROR:",
        err
      );
    }
  };

  // =====================================
  // TOGGLE PLAYLIST
  // =====================================

  const togglePlaylist = async (
    playlistId
  ) => {

    if (
      openPlaylistId === playlistId
    ) {

      setOpenPlaylistId(null);

      return;
    }

    setOpenPlaylistId(
      playlistId
    );

    if (
      !videosMap[playlistId]
    ) {

      await loadVideos(
        playlistId
      );
    }
  };

  // =====================================
  // RENDER
  // =====================================

  return (

    <div
      style={{
        maxWidth: "700px",
        margin: "0 auto",
      }}
    >

      <PlaylistHeader
        dailyTarget={
          dailyTarget
        }
      />

      <DndContext
        collisionDetection={
          closestCenter
        }
      >

        <SortableContext
          items={items.map(
            (i) => i.id
          )}
          strategy={
            verticalListSortingStrategy
          }
        >

          {items.map((item) => (

            <div
              key={item.id}
            >

              <PlaylistCard
                id={item.id}
                {...item}
                onClick={() =>
                  togglePlaylist(
                    item.id
                  )
                }
              />

              {openPlaylistId ===
                item.id && (

                <div
                  style={{
                    paddingLeft:
                      "20px",
                    marginTop:
                      "10px",
                  }}
                >

                  {(videosMap[
                    item.id
                  ] || []).map(
                    (video) => (

                      <VideoItem
                        key={
                          video.video_id
                        }
                        video={video}
                        playlistId={
                          item.id
                        }
                        selectedVideo={
                          selectedVideo
                        }
                        setSelectedVideo={
                          setSelectedVideo
                        }
                      />

                    )
                  )}

                </div>

              )}

            </div>

          ))}

        </SortableContext>

      </DndContext>

    </div>
  );
}