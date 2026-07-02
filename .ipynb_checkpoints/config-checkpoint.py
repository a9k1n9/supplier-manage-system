{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b2ae35cc-af70-4000-aa58-47e23d1661cb",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name '__file__' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 3\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m os\n\u001b[32m      2\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m3\u001b[39m \u001b[38;5;28;01mclass\u001b[39;00m Config:\n\u001b[32m      4\u001b[39m     SECRET_KEY = os.environ.get(\u001b[33m'SECRET_KEY'\u001b[39m) \u001b[38;5;28;01mor\u001b[39;00m \u001b[33m'dev-key-123'\u001b[39m\n\u001b[32m      5\u001b[39m     SQLALCHEMY_DATABASE_URI = os.environ.get(\u001b[33m'DATABASE_URL'\u001b[39m) \u001b[38;5;28;01mor\u001b[39;00m \u001b[33m'sqlite:///'\u001b[39m + os.path.join(os.path.abspath(os.path.dirname(__file__)), \u001b[33m'instance'\u001b[39m, \u001b[33m'company.db'\u001b[39m)\n\u001b[32m      6\u001b[39m     SQLALCHEMY_TRACK_MODIFICATIONS = \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 5\u001b[39m, in \u001b[36mConfig\u001b[39m\u001b[34m()\u001b[39m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m os\n\u001b[32m      4\u001b[39m \n\u001b[32m----> \u001b[39m\u001b[32m5\u001b[39m \u001b[38;5;28;01mclass\u001b[39;00m Config:\n\u001b[32m      6\u001b[39m     SECRET_KEY = os.environ.get(\u001b[33m'SECRET_KEY'\u001b[39m) \u001b[38;5;28;01mor\u001b[39;00m \u001b[33m'dev-key-123'\u001b[39m\n\u001b[32m      7\u001b[39m     SQLALCHEMY_DATABASE_URI = os.environ.get(\u001b[33m'DATABASE_URL'\u001b[39m) \u001b[38;5;28;01mor\u001b[39;00m \u001b[33m'sqlite:///'\u001b[39m + os.path.join(os.path.abspath(os.path.dirname(__file__)), \u001b[33m'instance'\u001b[39m, \u001b[33m'company.db'\u001b[39m)\n\u001b[32m      8\u001b[39m     SQLALCHEMY_TRACK_MODIFICATIONS = \u001b[38;5;28;01mFalse\u001b[39;00m\n",
      "\u001b[31mNameError\u001b[39m: name '__file__' is not defined"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "class Config:\n",
    "    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'\n",
    "    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'company.db')\n",
    "    SQLALCHEMY_TRACK_MODIFICATIONS = False\n",
    "    PER_PAGE = 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbecfe61-53f3-42d6-954f-e70d28f06a96",
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
