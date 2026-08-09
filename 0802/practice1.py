# ============================================================
# Practice 1 - 學生成績管理系統
# 涵蓋：變數、list、dict、迴圈、函式、條件判斷、例外處理
# ============================================================

# --- 資料定義 ---
students = [
    {"name": "Alice",   "scores": [85, 92, 78, 90]},
    {"name": "Bob",     "scores": [60, 55, 70, 65]},
    {"name": "Carol",   "scores": [95, 98, 100, 92]},
    {"name": "David",   "scores": [40, 50, 45, 55]},
    {"name": "Eve",     "scores": [75, 80, 72, 88]},
]


# --- 函式定義 ---

def average(scores: list[float]) -> float:
    """計算平均分數"""
    if not scores:
        raise ValueError("成績串列不能為空")
    return sum(scores) / len(scores)


def grade(avg: float) -> str:
    """依平均分數回傳等第"""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def analyze(students: list[dict]) -> list[dict]:
    """
    分析每位學生的成績，回傳包含平均與等第的結果列表
    """
    results = []
    for s in students:
        try:
            avg = average(s["scores"])
            results.append({
                "name":    s["name"],
                "avg":     round(avg, 1),
                "grade":   grade(avg),
                "highest": max(s["scores"]),
                "lowest":  min(s["scores"]),
            })
        except ValueError as e:
            print(f"[警告] {s['name']} 的資料有誤：{e}")
    return results


def print_report(results: list[dict]) -> None:
    """印出成績報表"""
    header = f"{'姓名':<8} {'平均':>6} {'等第':>4} {'最高':>6} {'最低':>6}"
    print("=" * len(header))
    print("         學生成績報表")
    print("=" * len(header))
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['name']:<8} {r['avg']:>6} {r['grade']:>4} {r['highest']:>6} {r['lowest']:>6}")
    print("=" * len(header))


def class_summary(results: list[dict]) -> None:
    """印出全班統計摘要"""
    avgs = [r["avg"] for r in results]
    grade_counts: dict[str, int] = {}
    for r in results:
        grade_counts[r["grade"]] = grade_counts.get(r["grade"], 0) + 1

    print("\n📊 全班統計")
    print(f"  人數      : {len(results)} 人")
    print(f"  全班平均  : {sum(avgs) / len(avgs):.1f}")
    print(f"  最高平均  : {max(avgs)}（{next(r['name'] for r in results if r['avg'] == max(avgs))}）")
    print(f"  最低平均  : {min(avgs)}（{next(r['name'] for r in results if r['avg'] == min(avgs))}）")
    print(f"  等第分布  : { {k: grade_counts[k] for k in sorted(grade_counts)} }")


# --- 主程式 ---

if __name__ == "__main__":
    results = analyze(students)
    print_report(results)
    class_summary(results)
