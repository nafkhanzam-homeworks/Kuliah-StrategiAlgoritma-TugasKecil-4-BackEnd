import express, { Response, Request } from "express";
import { spawn } from "child_process";

const app = express();
const port = process.env.PORT ?? 3000;

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
};

app.use(express.json());

app.use(
    "/",
    (req: SearchRequest, res: Response<SearchResponseBody | string>) => {
        console.log(JSON.stringify(req.body));
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
            if (error) {
                res.send(error);
            } else {
                res.send(JSON.parse(result));
            }
        });
    },
);

app.listen(port, () => {
    console.log(`Listening on port ${port}...`);
});
