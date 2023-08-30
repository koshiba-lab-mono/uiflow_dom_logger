import React, {
  useRef,
  MouseEventHandler,
  Dispatch,
  SetStateAction,
} from "react";
import Button from "@mui/material/Button";

type PropType = {
  setFile: Dispatch<SetStateAction<File | null>>;
};

export const UploadButton = ({ setFile }: PropType) => {
  const inputRef = useRef<HTMLInputElement>(null);

  const inputOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.currentTarget.files;
    if (!files || !files.length) {
      return;
    }
    const file = files[0];
    setFile(file);
  };

  return (
    <>
      <Button
        variant="contained"
        color="success"
        onClick={() => inputRef.current?.click()}
      >
        upload
        <input hidden ref={inputRef} type="file" onChange={inputOnChange} />
      </Button>
    </>
  );
};
