import Dexie from "dexie";
import { ContentStore, ContentType } from "./contentStore";

type BlockDexie = Dexie & {
  blocks: Dexie.Table<ContentType, number>;
};

export class IndexedDBStore extends ContentStore {
  private db: BlockDexie | null;

  private constructor() {
    super();
    this.db = null;
  }

  static async createInstance() {
    const instance = new IndexedDBStore();
    instance.db = new Dexie("blockdb") as BlockDexie;
    instance.db.version(1).stores({
      blocks: "date,content",
    });

    return instance;
  }

  public async add(content: ContentType): Promise<void | ContentType> {
    if (!this.db) {
      return;
    }

    const res = await this.db.blocks.put(content).catch((err) => {
      console.log(err);
    });

    return content;
  }

  public async getAll() {
    if (!this.db) {
      return [];
    }

    return await this.db.blocks.toArray();
  }

  public async deleteAll(): Promise<void> {
    if (!this.db) {
      return;
    }

    return await this.db.blocks.clear();
  }
}
