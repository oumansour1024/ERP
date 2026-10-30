from odoo import fields, models


class SchoolTrack(models.Model):
    _name = "school.track"
    _description = "Academic track"
    _order = "name"

    name = fields.Char(required=True)
    code = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)
    student_ids = fields.One2many("school.student", "track_id", string="Students")
    student_count = fields.Integer(compute="_compute_student_count")

    _sql_constraints = [
        ("name_unique", "UNIQUE(name)", "The track name must be unique."),
    ]

    def _compute_student_count(self):
        student_data = self.env["school.student"].read_group(
            [("track_id", "in", self.ids)],
            ["track_id"],
            ["track_id"],
        )
        counts = {
            item["track_id"][0]: item["track_id_count"]
            for item in student_data
            if item.get("track_id")
        }
        for track in self:
            track.student_count = counts.get(track.id, 0)


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student"
    _order = "name"

    name = fields.Char(string="Full Name", required=True)
    reference = fields.Char(required=True, copy=False, default="New")
    birth_date = fields.Date(string="Date of Birth")
    email = fields.Char()
    phone = fields.Char()
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ]
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("enrolled", "Enrolled"),
            ("graduated", "Graduated"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        required=True,
    )
    track_id = fields.Many2one(
        "school.track",
        string="Academic Track",
        ondelete="restrict",
    )
    notes = fields.Text()
    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            "reference_unique",
            "UNIQUE(reference)",
            "The student reference must be unique.",
        ),
    ]
