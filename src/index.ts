import express, { Response, Request } from "express";
import { exec } from "child_process";

const app = express();
const port = process.env.PORT ?? 3000;

interface SearchRequest extends Request {
    body: {
        text: string
    }
}

// type SearchResponseBody = {
//     date: Date
// };

app.use("/", express.json(), (req: SearchRequest, res: Response<string>) => {
    exec(`python alg/main.py ${req.body.text}`, (err, stdout, stderr) => {
        if (err) {
            console.log(err);
            return res.status(500).send("Internal server error!");
        }
        if (stderr) {
            console.log(stderr);
        }
        return res.send(stdout);
    });
});

app.listen(port, () => {
    console.log(`Listening on port ${port}...`);
});
