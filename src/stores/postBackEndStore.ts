import { ContentStore, ContentType } from "./contentStore";

export class PostBackEndStore extends ContentStore {
  constructor(private host: string) {
    super();
  }

  public async add(content: { date: number; html: string }) {
    const res = await fetch(this.host, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(content),
    }).catch((err) => {
      throw err;
    });

    return content;
  }
  public async getAll() {
    return [];
  }

  public async deleteAll(): Promise<void> {
    return;
  }
}
