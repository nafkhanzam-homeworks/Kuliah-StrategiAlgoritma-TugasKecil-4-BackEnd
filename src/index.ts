import { spawn } from "child_process";
import cors from "cors";
import express, { Request, Response } from "express";

interface SearchRequest extends Request {
    body: {
        text: string;
        keyword: string;
        algorithm: "Boyer-Moore" | "KMP" | "Regex";
    };
}

type SearchResponseBody = {
    time: string;
    count: number;
    sentence: string;
    index_found: number;
}[];

const app = express();
const port = process.env.PORT ?? 3000;

app.use(cors());
app.use(express.json());

app.use(
    "/",
    (req: SearchRequest, res: Response<SearchResponseBody | string>) => {
        const process = spawn("python", [
            "src/algorithm/main.py",
            JSON.stringify(req.body),
        ]);
        let result = "";
        let error = "";
        process.stdout.on("data", (data) => {
            result += data;
        });
        process.stderr.on("data", (data) => {
            error += data;
        });
        process.stdout.on("end", () => {
            if (error && !result) {
                res.status(400).send(error);
            } else {
                try {
                    res.json(JSON.parse(result));
                } catch (err) {
                    res.status(500).send("Parsing JSON failed!");
                }
            }
        });
    },
);

app.listen(port, () => {
    console.log(`Listening on port ${port}...`);
});
