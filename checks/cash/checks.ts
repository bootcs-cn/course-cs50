/**
 * Cash 评测检查
 *
 * 迁移自 CS50 problems/cash/__init__.py
 */
import { Checks, Check, exists, run } from "bootcs";
import { compile } from "bootcs/c";

// 生成硬币数量的正则表达式（确保不与其他数字混淆）
function coins(num: number): string {
  return `(?<!\\d)${num}(?!\\d)`;
}

export default class CashChecks extends Checks {
  @Check({ description: "cash.c exists" })
  async exists() {
    exists("cash.c");
  }

  @Check({ description: "cash.c compiles", dependency: "exists" })
  async compiles() {
    await compile("cash.c", { lcs50: true });
  }

  @Check({ description: "input of 41 yields output of 4", dependency: "compiles" })
  async test041() {
    await run("./cash").stdin("41").stdout(coins(4), "4\n").exit(0);
  }

  @Check({ description: "input of 1 yields output of 1", dependency: "compiles" })
  async test001() {
    await run("./cash").stdin("1").stdout(coins(1), "1\n").exit(0);
  }

  @Check({ description: "input of 15 yields output of 2", dependency: "compiles" })
  async test015() {
    await run("./cash").stdin("15").stdout(coins(2), "2\n").exit(0);
  }

  @Check({ description: "input of 160 yields output of 7", dependency: "compiles" })
  async test160() {
    await run("./cash").stdin("160").stdout(coins(7), "7\n").exit(0);
  }

  @Check({ description: "input of 2300 yields output of 92", dependency: "compiles" })
  async test230() {
    await run("./cash").stdin("2300").stdout(coins(92), "92\n").exit(0);
  }

  @Check({ description: "rejects a negative input like -1", dependency: "compiles" })
  async test_reject_negative() {
    await run("./cash").stdin("-1").reject();
  }

  @Check({ description: 'rejects a non-numeric input of "foo"', dependency: "compiles" })
  async test_reject_foo() {
    await run("./cash").stdin("foo").reject();
  }

  @Check({ description: 'rejects a non-numeric input of ""', dependency: "compiles" })
  async test_reject_empty() {
    await run("./cash").stdin("").reject();
  }
}
