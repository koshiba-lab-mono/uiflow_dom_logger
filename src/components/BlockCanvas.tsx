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

    const wrapBlockChunks = divRef.current.children[0];
    Array.from(wrapBlockChunks.children).forEach((div) => {
      const svg = div.children[0];
      const blockChunk = svg.children[0];
      const { width, height } = blockChunk.getBoundingClientRect();
      svg.setAttribute("width", String(width));
      svg.setAttribute("height", String(height));
    });
  }, [contentState]);

  const parseOptions: HTMLReactParserOptions = {
    htmlparser2: {
      lowerCaseTags: false,
    },
    replace: (node) => {
      if (
        node instanceof Element &&
        node.parent instanceof Element &&
        node.parent.attribs.class == "blocklyBlockCanvas"
      ) {
        // transformの属性を消し，gタグはdiv, svgで内包する
        node.attribs.transform = "";
        return (
          <div>
            <svg>{domToReact([node])}</svg>
          </div>
        );
      }
    },
  };

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
      <div ref={divRef}>{parse(contentState.html, parseOptions)}</div>
    </>
  );
};
