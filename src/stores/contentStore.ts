export type ContentType = {
  date: number;
  html: string;
};

export abstract class ContentStore {
  public abstract add(content: ContentType): Promise<void | ContentType>;
  public abstract getAll(): Promise<ContentType[]>;
  public abstract deleteAll(): Promise<void>;
}
