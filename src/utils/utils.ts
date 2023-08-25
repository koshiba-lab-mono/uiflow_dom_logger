export const wrapDivSvg = (element: Element) => {
  const wrapDiv = document.createElement("div");
  const wrapSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  const rect = element.getBoundingClientRect();
  wrapSvg.setAttribute("width", String(rect.width));
  wrapSvg.setAttribute("height", String(rect.height));
  wrapSvg.appendChild(element);
  wrapDiv.appendChild(wrapSvg);
  return wrapDiv;
};
