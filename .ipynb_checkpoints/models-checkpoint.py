{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "50f57c27-ef3b-453d-872d-5e0760f5aed4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask_sqlalchemy import SQLAlchemy\n",
    "from datetime import datetime\n",
    "\n",
    "db = SQLAlchemy()\n",
    "\n",
    "class Company(db.Model):\n",
    "    __tablename__ = 'company'\n",
    "    id = db.Column(db.Integer, primary_key=True, autoincrement=True)\n",
    "    seq = db.Column(db.Integer, nullable=True)\n",
    "    name = db.Column(db.String(200), nullable=False)\n",
    "    status = db.Column(db.String(50))\n",
    "    legal_rep = db.Column(db.String(100))\n",
    "    phone = db.Column(db.String(50))\n",
    "    capital = db.Column(db.String(50))\n",
    "    establish_date = db.Column(db.Date)\n",
    "    credit_code = db.Column(db.String(50), unique=True)\n",
    "    address = db.Column(db.String(300))\n",
    "    org_type = db.Column(db.String(100))\n",
    "    industry = db.Column(db.String(100))\n",
    "    intro = db.Column(db.Text)\n",
    "    scope = db.Column(db.Text)\n",
    "    business_term = db.Column(db.String(100))\n",
    "    scale = db.Column(db.String(50))\n",
    "    cert = db.Column(db.String(200))\n",
    "    in_supplier_list = db.Column(db.Boolean, default=False)\n",
    "    is_defaulted = db.Column(db.Boolean, default=False)\n",
    "    business_scope = db.Column(db.String(100))\n",
    "    created_at = db.Column(db.DateTime, default=datetime.now)\n",
    "    updated_at = db.Column(db.DateTime, onupdate=datetime.now)\n",
    "\n",
    "    def to_dict(self):\n",
    "        from datetime import date\n",
    "        d = {}\n",
    "        for col in self.__table__.columns:\n",
    "            val = getattr(self, col.name)\n",
    "            if isinstance(val, datetime):\n",
    "                val = val.strftime('%Y-%m-%d %H:%M:%S')\n",
    "            elif isinstance(val, date):\n",
    "                val = val.strftime('%Y-%m-%d')\n",
    "            d[col.name] = val\n",
    "        return d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3123bdfd-86dc-44be-b16f-8c532c1e7142",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
