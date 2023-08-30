import React, { useEffect, useRef } from "react";
import parse, { HTMLReactParserOptions, domToReact } from "html-react-parser";
import { ContentType } from "../stores/contentStore";
import { Element } from "html-react-parser";

type PropsType = {
  contentState: ContentType;
};

export const BlockCanvas = ({ contentState }: PropsType) => {
  const divRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!divRef.current) {
      return;
    }

    Array.from(divRef.current.children!).forEach((div) => {
      const svg = div.children[0];
      const g = svg.children[0];
      const { width, height } = g.getBoundingClientRect();
      svg.setAttribute("width", String(width));
      svg.setAttribute("height", String(height));
    });

    contentState.html = divRef.current.innerHTML;
  }, [contentState]);

  const date = new Date(contentState.date);
  const formattedDate = date.toLocaleDateString("ja", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });

  return (
    <>
      <h1>{formattedDate}</h1>
      <div ref={divRef}>{parse(contentState.html)}</div>
    </>
  );
};
