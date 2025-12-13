/**
 * Mario (Less) 评测检查
 *
 * 迁移自 CS50 problems/mario/less/__init__.py
 */
import { Checks, Check, exists, include, run, Failure } from "bootcs";
import { compile } from "bootcs/c";
import * as fs from "fs";

// 期望输出
const PYRAMIDS: Record<number, string> = {
  1: "#\n",
  2: " #\n##\n",
  8: "       #\n      ##\n     ###\n    ####\n   #####\n  ######\n #######\n########\n",
};

function checkPyramid(output: string, expected: string): void {
  if (output === expected) {
    return;
  }

  const outputLines = output.split("\n").filter((line) => line !== "");
  const expectedLines = expected.split("\n").filter((line) => line !== "");

  let help: string | undefined;
  if (outputLines.length === expectedLines.length) {
    if (
      outputLines.every(
        (ol, i) => ol.trimEnd() === expectedLines[i]
      )
    ) {
      help = "did you add too much trailing whitespace to the end of your pyramid?";
    } else if (
      outputLines.every((ol, i) => ol.slice(1) === expectedLines[i])
    ) {
      help = "are you printing an additional character at the beginning of each line?";
    }
  }

  throw new Failure(`Expected pyramid does not match output`, { help });
}

export default class MarioLessChecks extends Checks {
  @Check({ description: "mario.c exists" })
  async exists() {
    exists("mario.c");
  }

  @Check({ description: "mario.c compiles", dependency: "exists" })
  async compiles() {
    await compile("mario.c", { lcs50: true });
  }

  @Check({ description: "rejects a height of -1", dependency: "compiles" })
  async test_reject_negative() {
    await run("./mario").stdin("-1").reject();
  }

  @Check({ description: "rejects a height of 0", dependency: "compiles" })
  async test0() {
    await run("./mario").stdin("0").reject();
  }

  @Check({ description: "handles a height of 1 correctly", dependency: "compiles" })
  async test1() {
    const result = await run("./mario").stdin("1").stdout();
    checkPyramid(result, PYRAMIDS[1]);
  }

  @Check({ description: "handles a height of 2 correctly", dependency: "compiles" })
  async test2() {
    const result = await run("./mario").stdin("2").stdout();
    checkPyramid(result, PYRAMIDS[2]);
  }

  @Check({ description: "handles a height of 8 correctly", dependency: "compiles" })
  async test8() {
    const result = await run("./mario").stdin("8").stdout();
    checkPyramid(result, PYRAMIDS[8]);
  }

  @Check({
    description: 'rejects a height of -1, then accepts height of 2',
    dependency: "compiles",
  })
  async test9() {
    const result = await run("./mario").stdin("-1").reject().stdin("2").stdout();
    checkPyramid(result, PYRAMIDS[2]);
  }

  @Check({ description: 'rejects a non-numeric height of "foo"', dependency: "compiles" })
  async test_reject_foo() {
    await run("./mario").stdin("foo").reject();
  }

  @Check({ description: 'rejects a non-numeric height of ""', dependency: "compiles" })
  async test_reject_empty() {
    await run("./mario").stdin("").reject();
  }
}
