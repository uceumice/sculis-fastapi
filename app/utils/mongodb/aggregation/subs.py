# aggregation helper
class Aggregation:
    def __init__(self, date, filters=None) -> None:
        self.aggr = []
        self.date = date
        self.filters = filters

    def appl(self):
        return self.aggr

    def find_one(self):
        aggr_ = [
            {
                "$match": {
                    "metas._": self.date
                }
            },
            {
                "$limit": 1
            }
        ]
        self.aggr.extend(aggr_)
        return self

    def project(self):
        aggr_ = [
            {
                "$project": {
                    "_id": 0,
                    "subst": 1
                }
            }
        ]
        self.aggr.extend(aggr_)
        return self

    def filters_(self):

        def filter_prep():
            if not self.filters:
                return []

            return [
                {
                    "$and": [
                        {
                            "$in": [
                                "$$entry.subject",
                                [
                                    filt_["sid"]
                                ]
                            ]
                        },
                        {
                            "$in": [
                                "$$entry.group",
                                [
                                    filt_["gid"]
                                ]
                            ]
                        }
                    ],
                } for filt_ in self.filters
            ]

        aggr_ = [
            {
                "$project": {
                    "subst": {
                        "$map": {
                            "input": "$subst",
                            "as": "block",
                            "in": {
                                "class_": "$$block.class_",
                                "entries": {
                                    "$filter": {
                                        "input": "$$block.entries",
                                        "as": "entry",
                                        "cond": {
                                            "$or": filter_prep()
                                        }
                                    }
                                }

                            }
                        }
                    }
                }
            },
        ]
        if self.filters:
            self.aggr.extend(aggr_)
        return self

    def clean_empty(self):
        aggr_ = [
            {
                "$project": {
                    "subst": {
                        "$filter": {
                            "input": "$subst",
                            "as": "block",
                            "cond": {
                                "$ne": [
                                    {"$size": "$$block.entries"},
                                    0
                                ]
                            }
                        }
                    }
                }
            }
        ]
        self.aggr.extend(aggr_)
        return self
