/**
 * Hello 评测检查
 *
 * 迁移自 CS50 problems/hello/__init__.py
 */
import { Checks, Check, exists, run } from "bootcs";
import { compile } from "bootcs/c";

export default class HelloChecks extends Checks {
  @Check({ description: "hello.c exists" })
  async exists() {
    exists("hello.c");
  }

  @Check({ description: "hello.c compiles", dependency: "exists" })
  async compiles() {
    await compile("hello.c", { lcs50: true });
  }

  @Check({ description: "responds to name Emma", dependency: "compiles" })
  async emma() {
    await run("./hello").stdin("Emma").stdout("Emma").exit();
  }

  @Check({ description: "responds to name Rodrigo", dependency: "compiles" })
  async rodrigo() {
    await run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit();
  }
}
