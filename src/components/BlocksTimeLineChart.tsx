import React from "react";
import { Chart } from "chart.js";
import { registerables } from "chart.js";
import { ContentType } from "../stores/contentStore";
import { useRef } from "react";
import { Bar, getElementAtEvent } from "react-chartjs-2";
import { getBlockNum } from "../utils/utils";

type PropsType = {
  allData: ContentType[];
  dataOnClick?: (x: number) => void;
};

Chart.register(...registerables);

export const BlocksTimeLineChart = ({ allData, dataOnClick }: PropsType) => {
  const chartRef = useRef<Chart<"bar">>(null);

  const chartOnClick = (event: any) => {
    if (!dataOnClick) {
      return;
    }

    if (!chartRef.current) {
      return;
    }

    const [clickedData] = getElementAtEvent(chartRef.current, event);
    dataOnClick(clickedData.index);
  };

  const data = {
    labels: allData.map((content) =>
      new Date(content.date).toLocaleDateString("ja", {
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
      })
    ),
    datasets: [
      {
        label: "Block num",
        data: allData.map((content) => getBlockNum(content)),
        backgroundColor: "black",
      },
    ],
  };

  return (
    <>
      <Bar data={data} ref={chartRef} onClick={chartOnClick} />
    </>
  );
};
