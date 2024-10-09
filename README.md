<h1>Install</h1>

<p>pip install -r ./requirements.txt</p>

<h1>Run</h1>

<p>uvicorn main:app --reload</p>
<hr />
<h1>Docker</h1>

<h3>Build</h3>
<p>docker build -t fastapi-docker .</p>

<h3>Run</h3>
<p>docker run -d -p 80:80 fastapi-docker</p>
