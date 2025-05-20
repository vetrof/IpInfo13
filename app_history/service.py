# -*- coding: utf-8 -*-
from app_history.repository import HistoryRepo


def history_servise():
    data = HistoryRepo.all_history()
    return data

