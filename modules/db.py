from sqlalchemy import create_engine, text

def get_engine(db_url):
    return create_engine(db_url, pool_pre_ping=True)

def insert_trip(engine, origin, destination, distance, co2):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO trips (origin, destination, distance_km, co2_g) VALUES (:o, :d, :dist, :co2)"),
            {"o": origin, "d": destination, "dist": distance/1000, "co2": co2}
        )
