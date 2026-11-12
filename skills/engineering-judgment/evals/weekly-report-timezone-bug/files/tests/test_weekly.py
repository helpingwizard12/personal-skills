import unittest
from datetime import date

from reports.weekly import weekly_event_counts


class WeeklyCountsTest(unittest.TestCase):
    def test_counts_per_week_utc_user(self):
        # 2026-03-02 is a Monday. 12:00 UTC on Mon 2 Mar, Wed 4 Mar, and Mon 9 Mar.
        ts = [1772452800, 1772625600, 1773057600]
        self.assertEqual(
            weekly_event_counts(ts, "UTC"),
            {date(2026, 3, 2): 2, date(2026, 3, 9): 1},
        )


if __name__ == "__main__":
    unittest.main()
